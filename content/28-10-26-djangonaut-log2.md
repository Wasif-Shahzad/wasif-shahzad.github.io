Title: Djangonaut Space Log 2: Struggles to find the issue
Date: 2026-10-28 22:00
Category: Open-Source Software, Django, Django Debug Toolbar, Djangonaut Space
Tags: Django, Djangonaut-Space
Summary: My struggles and how my navigator helped me.
Featured: True

> This blog is the continuation of Log-1 of my Djangonaut Space session 7. I highly suggest reading that first to get some context. You may read it [here]({filename}21-10-26-djangonaut-space.md).

Last time around, I finished on `history_tr.html` where I found the form responsible for the "switch" button in the History Panel. After that, I searched the URL name attached to that form's action and landed on [this view](https://github.com/django-commons/django-debug-toolbar/blob/main/debug_toolbar/panels/history/views.py#L14). 

I started reading the view, added some print statements to make sense of what is happening and what is not. It did not take me long to see this line and what was happening here:

```py
for panel in toolbar.panels:
    # The 2 lines below
    if exclude_history and not panel.is_historical:
        continue
```

Every panel was being sent a new context but two panels weren't; the history panel and the redirects panel (I hope I remember the second one correctly). And after that I spent a lot of hours in total just staring at this view and what is happening here. I even spent over an hour of PyCharm debugger session at this loop. That's when I saw that the History Panel correctly gets the updated subtitle but it never updates and that was a bit weird. 

I reported that to Velda, and at that point I was blank. I did not have much clue on what to do.

I was feeling a bit disappointed in myself that I could not do this. The same night I was talking to Tim Schilling, an amazing guy and the guy who got me started with contributions to Django, and he told me that I could ask the navigator and the captain and even the team for pair programming sessions. It was not necessary that they would have the time but I certainly could try asking this.

And I did ask Velda, and thanksfully, she said she can do so. 

> Now before continuing, I wanna add a little disclaimer about a part Velda told and I, deliberately, did not write above. Right at the beginning, she told me to look into a file `history.js` and for some reason because of the superintelligence that I have, I decided to only debug `history/views.py` and got stuck. 

She showed me the entire process through which she reached different files such as `history_tr.html`, `history.js`, `utils.js` etc. Then, she made me go through the lines of the code right as a teacher would guide a student by holding his finger. And, at the end, I was able to understand what the functions inside `history.js` and `utils.js` do, or at least the functions that are concerned with the issue that I am working on.

Oh, and btw, I missed one of the two issues that were there. In the last blog I explained what the issue was with "switch" button but there was another issue which I never ever touched for some reason. I never knew about that issue until Velda told me about that in our pair programming session. 

This issue was that once we refresh the panel or switch panel and come back to history panel (basically another way which triggers the refresh action), the highlighted row was no more highlighted. Or in more technical terms, the row which previously had the `djdt-highlighted` HTML class did not have it any more.

At the end, I had known that the issue was a javascript issue and where it was. She suggested me a solution for both the issues and I wrote the comments on the lines where she suggested changes. (Comments still exist as part of my draft PR. [Link](https://github.com/django-commons/django-debug-toolbar/pull/2517/changes#diff-353376fd3d9a230e3fca00b62250ea90c0d8628a66a931e5a2365eb1129b0b57R19))

We had a session of almost 1 hour and 20 minutes and it was a wonderful experience. I am really thankful to Velda for helping me.

Then I started working a bit the next night, it was almost 9:00 PM (after our weekly meeting), I was tired because I had university too but I wanted to do something that night because I knew I will not have enough time in the upcoming days because of exams. Therefore, I kept working. 

For the refresh issue, the issue was here:
```js
function refreshHistory() {
    const formTarget = djDebug.querySelector(".refreshHistory");
    const container = djDebug.querySelector("#djdtHistoryRequests");
    const oldIds = new Set(
        pluckData(
            container.querySelectorAll("tr[data-request-id]"),
            "requestId"
        )
    );

    ajaxForm(formTarget)
        .then((data) => {
            // Remove existing rows first then re-populate with new data
            for (const node of container.querySelectorAll(
                "tr[data-request-id]"
            )) {
                node.remove();
            }
            for (const request of data.requests) {
                container.innerHTML = request.content + container.innerHTML;
            }
        })
```

As you can see, we remove old table rows and create them again but guess what, we never dealt with the `djdt-highlighted` class. It was never added again and hence, our highlight was gone missing. 

The fix was simple that we iterate over the rows, match the `request-id` of the row with our `current-request-id` and just add it to the classList but I did not know where the `current-request-id` was. It was a small "console.log()"-ing session and at the end I found out that our global element `djDebug` (which is the outermost container as well) has the `current-request-id` attached with it. And after this, I just did what I described above with that and wohooo! I had the refresh bug fixed. I literally jumped out of the chair and lightly screamed "YESS!". It was such a delight. 

And then I just opened a draft PR and went to sleep.

See you all until the next time!
