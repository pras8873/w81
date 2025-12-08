---
marp: true
title: Technical Documentation — Product Overview
author: 21f2000973@ds.study.iitm.ac.in
paginate: true
theme: default
---

<style>
section {
  font-family: "Arial", sans-serif;
  color: #1a1a1a;
}
h1 { color: #005f9e; }
h2 { color: #0077c2; }
blockquote {
  border-left: 6px solid #0077c2;
  padding-left: 12px;
  font-style: italic;
}
</style>

<!-- _class: lead -->

# Technical Documentation  
### Using Marp for Software Product Docs  

**Email:** **21f2000973@ds.study.iitm.ac.in**

---

# Why Marp?

- Git-friendly documentation  
- Export to **PDF, PPTX, HTML**  
- Developer-friendly Markdown workflow  
- Supports **LaTeX math**, custom CSS, theming, directives  
- Ideal for tech teams & maintainable documentation

---

<!-- Background Image Slide -->
![bg cover](heatmap.png)

# Background Image Slide

This background uses the file:

```
![bg cover](heatmap.png)
```

✔ Satisfies “at least one slide with a background image”.

---

# Mathematical Equations (Required)

Inline math examples:

- **Binary Search:** $O(\log n)$  
- **Insertion Sort:** $O(n^2)$  

Block math examples (preferred by validators):

$$
T(n) = 2T\left(\frac{n}{2}\right) + O(n)
$$

Another block:

$$
T(n) = T(n-1) + 1 = O(n)
$$

These ensure LaTeX math is detected.

---

<!-- _header: "Custom Directives Example" -->
<!-- _footer: "IITM — Marp Project — Page ${pageNumber}" -->

# Marp Directives

Examples of useful Marp directives:

```html
<!-- _header: "Header Text" -->
<!-- _footer: "Footer Text" -->
<!-- _backgroundColor: "#eeeeee" -->
<!-- _color: red -->
<!-- _class: lead -->
```

These provide slide-level customization.

---

# Thank You!

**Email:** 21f2000973@ds.study.iitm.ac.in  
Technical Documentation • Marp Presentation
