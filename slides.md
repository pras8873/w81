
✔ This satisfies **"at least one slide with a background image"**  
✔ The file **heatmap.png** already exists in your repository  

---

# Mathematical Expressions

Marp supports LaTeX-style math:

### Algorithmic Complexity

- Binary search:  
  **$O(\log n)$**

- Merge sort:  
$$
T(n) = 2T\left(\frac{n}{2}\right) + O(n)
      = O(n \log n)
$$

- Linear recurrence:  
$$
T(n) = T(n-1) + O(1) = O(n)
$$

---

<!-- _header: "Product Documentation Demo" -->
<!-- _footer: "IITM • Marp Project • Page ${pageNumber}" -->

# Marp Directives

Useful directives include:

```html
<!-- _header: "Header text" -->
<!-- _footer: "Footer text" -->
<!-- _backgroundColor: "#efefef" -->
<!-- _class: lead -->
<!-- _color: red -->
