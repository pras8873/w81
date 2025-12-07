---
marp: true
---

# Product Documentation
## Strategy & Implementation

**Technical Writer:**
21f2000973@ds.study.iitm.ac.in

---

# 1. Version Control Strategy

We are moving to a "Docs as Code" approach. This allows us to use git for versioning.

* **Branching:** Main for production, feature branches for drafts.
* **Review:** Pull requests required for text changes.

*This slide uses the 'header' directive.*

---

# 2. Algorithmic Complexity

We must document the performance implications of our API.

**Search Complexity:**

$$
T(n) = O(n \log n) + k
$$

Where:
- $n$ is the dataset size.
- $k$ is the latency.

---

![bg right:40%](https://images.unsplash.com/photo-1461749280684-dccba630e2f6?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80)

# 3. Visual Style Guide

Our documentation uses specific imagery to guide users.

- **Screenshots:** 16:9 aspect ratio.
- **Diagrams:** MermaidJS support.
- **Icons:** SVG format only.

*Contact: 21f2000973@ds.study.iitm.ac.in*
