Title: Djangonaut Space Log 3: JS one-liners && backend
Date: 2026-11-13 18:30
Category: Open-Source Software, Django, Django Debug Toolbar, Djangonaut Space, Javascript, Backend, Python
Tags: Django, Djangonaut-Space
Summary: The review process of my PR so far!
Featured: True

> If you are new around here, I highly suggest reading [Part 1]({filename}21-10-26-djangonaut-space.md) and [Part 2]({filename}28-10-26-djangonaut-log2.md) of this series.

Last time around, at the end of Part 2, I had figured out a javascript fix, wrote the code and had pushed the changes. That allowed me to change the status of my PR from "draft" to "ready for review". And my first ever for the Django-Debug-Toolbar Pull Request was opened.

### JS one-liners

The first review of the PR came from [Johannes Maron](github.com/codingjoe) a.k.a "codingjoe". And his review was quite fascinating for me. Historically, I have written the most code in C++ and even in that, most of it is competitive programming (hereby referred to as "CP"). And in CP, the way you code does not matter. So elegance in the code isn't cared about that much. Because of my this experience, the javascript that I wrote for both the fixes was quite inefficient/inelegant. 

I realized this after codingjoe's comments and was left in an awe with how pretty that javascript was that he suggested. For instance, below is one such "JS-oneliner". (Red is me, Green is Joe)

```diff
- const history_rows = [...container.rows];
- const target_id = djDebug.getAttribute("data-request-id");
- history_rows.forEach((row) => {
-     const row_request_id = row.dataset.requestId;
-     if (row_request_id === target_id) {
-         row.classList.add("djdt-highlighted");
-     }
- });
+ container
+   .querySelector(
+       `tr[data-request-id="${djDebug.dataset.requestId}"]`
+   )
+   .classList.add("djdt-highlighted");
```

One more thing that I learnt in this process was how one can use `querySelector` and target a specific value for an HTML attribute. You can use the following syntax:
```js
container
  .querySelector('.outer-container .element[someAttribute="someValue"]');
```
You can, ofcourse, replace `"someValue"` with a variable like I have in the above diff. *Note that you will need to use backticks (\`\`) instead of double quotes ("")*

You can see more of the JS changes that I did, of similar type, in this [commit](https://github.com/django-commons/django-debug-toolbar/pull/2517/changes/f4d02eeeaa76a51ac13b577a1328a11b1051ccc5).

### Backend changes

Now, lets move on to the other part of the blog, the backend changes.

In [my djangonaut space log2]({filename}28-10-26-djangonaut-log2.md), I discussed the `history_sidebar` view which was being used by the API that the **switch** button is linked to. If you have read my previous blog you are probably familiar with this condition:

```py
for panel in toolbar.panels:
    # The 2 lines below
    if exclude_history and not panel.is_historical:
        continue
```

And you probably already know that this is the condition which blocks `HistoryPanel` to get added to the `context` being used to reconstruct the toolbar. And to move the "switch" button on the backend, the fix would be to simply add only the `panel_button` part of the `context` with HistoryPanel and not adding the `panel_content` part of the context. 

You might think that inside the if, we can find a way to recognize if its `HistoryPanel` or `RedirectsPanel`. Then render the button, add to `context` and that's it? Its this easy? Why is the fool writing this trying to overexplain?

Well, calm down sir... And because of your rant I am forced to write this next sentence in CAPS. YOU ARE ABSOLUTELY WRONG. (If you did not rant you can ofcourse ignore this XD)

What happens when you **only** add the `panel_button` to the context and don't add any `panel_content` is that the entire Panel disappears and only its button stays. Well... that's what you coded by *removing `panel_content`, didn't you?*

So, as you would have guessed, the fix is to somehow, someway set the `panel_content` for the `HistoryPanel` to the previously rendered context. Or in other words, don't change it. 

The issue is that the toolbar, at that time, didn't have any way to keep this persistency. (Credits to ChatGPT (Codex) for doing the search for me :P)

And, at that time, [Tim Schilling](github.com/tim-schilling) suggested me to add this method to the `Panel` class, which is the parent of every beautifully functioning panel that you see in the toolbar.

```py
    def _get_history_rerender_context(self):
        # Always rerender the button.
        context = {"button": render_to_string(
            "debug_toolbar/includes/panel_button.html", {"panel": self}
        )}
        if self.is_historical:
            context["content"] = render_to_string(
                "debug_toolbar/includes/panel_content.html", {"panel": self}
            )
        return context
```
We would also add a check inside the `replaceToolbarState` method in `utils.js` to update the content only if there was the content key in the context passed to it.

There was an investigation on migrating the refresh button fix to backend too but that seemed not good, so we decided to not go in that direction. Although, I have learnt a lot more about how the HistoryPanel works after that investigation and perhaps, spotted a few issues too.

### Closing

The changes after this were mostly about refactoring the code around the backend changes and that how it could be optimized but that part is not done yet so I will discuss that in the next blog which will be probably also say that **I have my PR merged, finally :sob:**. Moreover, I am yet to write the tests. I will need to write tests about the highlight persistency fix in refresh button on the frontend as well. That will be a lot of new learning as well because I haven't really ever written those many frontend tests. The only few that I wrote were at my internship but those were very small. 

I hope you enjoyed reading this!

Bye!
