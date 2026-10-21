Title: Smooth Scrolling with position: sticky;
Date: 2026-06-27 11:47
Category: CSS
Tags: Frontend, Web-dev, css
Authors: Wasif Shahzad
Summary: Explaining how sticky positioning creates cool scrolling effects.
Slug: smooth-scrolling-with-sticky-positioning-in-css
Featured: False

This is my first day of writing blogs. A series where I make a commitment to myself to write a blog each morning about what I learnt the day before so I can reiterate things and consolidate my learning.

### How I learnt about `position: sticky;`

I was going through [this template](https://sable-boil-40643239.figma.site/archive) (the template which I have used to create this blog website) and was trying to figure out the HTML structure and CSS styles through inspecting the elements. And then I saw that there was a certain `position: sticky;` which was a new thing for me. I had never seen it nor used it before.

Right away, I just copied that to my `style.css` and did not notice something very different. I just left it there while I was trying to figure out the flexbox. It remained there for a while. Meanwhile, I was awfully amazed by how the sidebar scrolls are kind of synchronized in the design. The left sidebar does not scroll down until we go to the bottom of the right sidebar which looked pretty cool at first. When I was done with the flexbox I noticed that that's precisely what my implementation was doing and I did not even realize. 

After being done with that, I searched about `position: sticky` and learnt what it is. 

### What is *sticky* positioning?

Sticky positioning is a hybrid between `fixed` and `relative` position. It switches between the two depending on the **scroll position**. 

For example, It can look like the container is `fixed` on the screen. But, when the scrolling position is reaching its bottom it goes above and switches to `relative` positioning creating a nice *behind the curtain* like scrolling animation. An animation similar to that on the linked template in Paragraph #2.

> Updating this on 23rd July, `sticky` positioning needs one of the `top, bottom, left, right` property to work otherwise, it doesn't work. So, keep that in mind and don't be dumb like me :)
