---
marp: true
title: Technical Documentation — Product Overview
author: 21f2000973@ds.study.iitm.ac.in
paginate: true
theme: default
---

<!-- External Web CSS Theme -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/marp-core/3.9.0/marp.min.css">

<style>
/* Custom Slide Styling Using Web CSS */
section {
  font-family: "Arial", sans-serif;
  color: #1a1a1a;
}
h1 {
  color: #005f9e;
}
h2 {
  color: #0077c2;
}
blockquote {
  border-left: 6px solid #0077c2;
  padding-left: 12px;
  font-style: italic;
}
</style>

<!-- _class: lead -->
# Technical Documentation  
### Built with Marp (Markdown Presentation System)  
#### **21f2000973@ds.study.iitm.ac.in**

---

# Why Marp?

Marp allows technical teams to:

- Maintain documentation in **version control**
- Export to **PDF / PPTX / HTML**
- Render code, math, and diagrams
- Use **themes** and **custom CSS**
- Keep technical slides close to source code

---

<!-- Background image from the web -->
<!-- _backgroundImage: "https://images.unsplash.com/photo-1518779578993-ec3579fee39f?auto=format&fit=crop&w=1200&q=60" -->
<!-- _backgroundSize: cover -->
<!-- _color: white -->

# Background Image Slide

This slide uses a high-resolution **web image** from Unsplash as the background.  
No local files are required.

---

# Mathematical Expressions

Marp supports **LaTeX math rendering** (KaTeX):

### Inline examples
- Binary search: $O(\log n)$  
- Matrix multiplication: $O(n^3)$  

### Recurrence example
$$
T(n) = 2T\left(\frac{n}{2}\right) + O(n)
\Rightarrow T(n) = O(n \log n)
$$

### Algorithmic Complexity Proof
$$
T(n) = T(n-1) + O(1)
\Rightarrow T(n) = O(n)
$$

---

<!-- _header: "Custom Directives Example" -->
<!-- _footer: "IITM • Marp Documentation • Page ${pageNumber}" -->

# Marp Directives

Directives allow per-slide customization:

```html
<!-- _header: "Slide Header" -->
<!-- _footer: "Footer Text" -->
<!-- _backgroundColor: #f0f0f0 -->
<!-- _color: red -->
