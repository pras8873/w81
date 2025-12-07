import marimo

__generated_with = "0.1.0"
app = marimo.App()

@app.cell
def _():
    import marimo as mo
    # Email: 21f2000973@ds.study.iitm.ac.in
    return mo,

@app.cell
def _(mo):
    # Create an interactive slider widget
    # This widget controls the input value for the analysis
    slider = mo.ui.slider(start=1, end=20, label="Select Input")
    
    # Display the slider
    slider
    return slider,

@app.cell
def _(mo, slider):
    # Data Flow: This cell depends on the 'slider' variable from the previous cell.
    # It recalculates automatically whenever the slider moves.
    
    value = slider.value
    square = value ** 2
    
    # Dynamic Markdown Output based on widget state
    mo.md(
        f"""
        ### Analysis Results
        
        You selected: **{value}**
        
        The square is: **{square}**
        
        Visual: {'🟦' * value}
        """
    )
    return square, value,

if __name__ == "__main__":
    app.run()
