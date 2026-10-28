Title: Djangonaut Space Session 7 so far... (Log 1)
Date: 2026-10-21 09:20
Category: Open-Source Software, Django, Django Debug Toolbar, Djangonaut Space
Tags: Django, Djangonaut-Space
Summary: How my first 2 weeks at Djangonaut space session 7 have gone.
Featured: True
<!--Cover: images/djangonaut-space-astrolaptop.png-->

It has been two weeks since Djangonaut space started and I wanted to post this blog from so long but couldn't due to other commitments but I am here writing this now.

First of all, I am extremely happy that I got selected into this program. Its an absolute pleasure to be here. I am really optimistic about my goals during this program which include increasing my understanding of Django (although this is not the only goal).

And to help me with that, I think I am in the perfect place possible as part of Team Norma, where I will contribute to the Django Debug Toolbar. Its been two weeks since I started here and joined the community and, as always, the community has been so so welcoming to everyone. I already feel like home.

We have had two team meetings with our Navigator, [Velda Kiara](https://github.com/VeldaKiara), and one meeting with our Captain, Amanda Savluchinske. 

In the first meeting, Velda briefed us with a small set of issues filtered out for this session and I picked [this issue](https://github.com/django-commons/django-debug-toolbar/issues/2455). Unfortunately, I could not get to work too much on it during week-1 (zero index weeks lol) because I was travelling to Islamabad to participation in NASCON '26, held at FAST NUCES, Islamabad. I only got 15-20 minutes to investigate what was going on and hereafter I will try to explain the issue and what I have found so far.

I tried to reproduce the bug locally and succesfully did this. In the history tab, when we use the "switch" button to switch to a different URL in the history, the subtitle under the "History" in the tabs doesn't **switch**. I used the example app provided in the Django Debug Toolbar to investigate this. It has only 2 URLs, `/` and `/__debug__`. When I switched by *changing* the URL in the search bar, it switches correctly but when I used the "switch" button, it did not work as intended.

Because, I was working on the example app, my approach to find the place where the bug is happening was to trace it from the example app. Therefore, I opened the template, found the history template. It further used a separate template for each `history_tr` so I opened that and saw that the following code is responsible for the "switch" button.

```html
<td class="djdt-actions">
  <form method="get" action="{% url 'djdt:history_sidebar' %}">
    {{ history_context.form.as_div }}
    <button type="button" data-request-id="{{ request_id }}" class="switchHistory">Switch</button>
  </form>
</td>
```

My next task is to go to the URLs for the example app and find where the `djdt:history_sidebar` URL leads to and investigate the issue further.

I will investigate it further today and write a follow up blog tomorrow or as soon as possible, but my goal is to get the PR open by the end of this week if nothing goes wrong!
