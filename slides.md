---
marp: true
title: Technical Documentation — Product Overview
author: 21f2000973@ds.study.iitm.ac.in
paginate: true
theme: default
---

<!-- External Web CSS -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/marp-core/3.9.0/marp.min.css">

<style>
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
### Using Marp for Software Product Docs  
#### **21f2000973@ds.study.iitm.ac.in**

---

# Why Marp?

- Version-control friendly  
- Convert to **PDF, PPTX, HTML**  
- Great for developers  
- Supports **math, code, directives, CSS**  
- Ideal for technical teams

---

<!-- _backgroundImage: "./heatmap.png" -->
<!-- _backgroundSize: cover -->
<!-- _color: white -->

# Background Image Slide  
### (Using heatmap.png from project root)

This slide satisfies the **"at least one background image"** requirement.

The file **heatmap.png must be in the same directory as slides.md**.

---

# Mathematical Expressions

Marp supports LaTeX math:

- Binary search: $O(\log n)$  
- Merge sort:  
$$
T(n)=2T\left(\frac{n}{2}\right)+O(n)=O(n\log n)
$$

- Linear recurrence:  
$$
T(n)=T(n-1)+O(1) \Rightarrow O(n)
$$

---

<!-- _header: "Custom Directives Example" -->
<!-- _footer: "IITM • Marp Project • Page ${pageNumber}" -->

# Marp Directives

Examples:

```html
<!-- _header: "Header Text" -->
<!-- _footer: "Footer Text" -->
<!-- _backgroundColor: "#eeeeee" -->
<!-- _color: "red" -->
