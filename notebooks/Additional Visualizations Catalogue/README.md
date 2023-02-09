# RAPIDS Accelerated Visualizations Catalog

# RAPIDS Compatible Visualization Libraries Catalog

Run the RAPIDS Viz Catalog notebook to interactively explore the below viz libraries and compare how easy it is to switch from cpu to gpu usage.

## Featured Libraries

- HoloViews: Declarative objects for quickly building complex interactive plots from high-level specifications. Directly uses cuDF.
- hvPlot: Quickly return interactive plots from cuDF, Pandas, Xarray, or other data structures. Just replace .plot() with .hvplot().
- Datashader: Rasterizing huge datasets quickly as scatter, line, geospatial, or graph charts. Directly uses cuDF.
- Plotly: Charting library that supports Plotly Dash for building complex analytics applications.
- Bokeh: Charting library for building complex interactive visualizations.
- Seaborn: Static single charting library that extends matplotlib.

## Other Notable Libraries

- cuxfilter: RAPIDS developed cross filtering dashboarding tool that integrates many of the libraries above.
- Panel: A high-level app and dashboarding solution for the Python ecosystem.
- PyDeck: Python bindings for interactive spatial visualizations with webGL powered deck.gl, optimized for a Jupyter environment.
- node RAPIDS: RAPIDS bindings in nodeJS, a high performance JS/TypeScript visualization alternative to using Python.

<<<<<<< HEAD
## Generate Static Charts from Notebook for Jekyll
**Note:** code for the apps are in the `/examples/` folder.

Be sure to replace `Charts().view()` with below to pre-compute and export each chart:
`Charts().view().save('chart-name.html', embed=True, embed_json=True, save_path="./data/", json_prefix="chart-JSON")`

Then run nbconvert to generate the wrapper page and manually add each exported chart:
=======
## Generate Static webpage from Notebook
>>>>>>> 1520692538cf556c6833e85856a148e23e819560

```bash
conda create -n viz-catalogue-env -c rapidsai -c conda-forge -c nvidia \
    cudf=22.12 datashader holoviews hvplot jupyterlab plotly python=3.9 seaborn

conda activate viz-catalogue-env

<<<<<<< HEAD
# export page
jupyter nbconvert --to markdown RAPIDS\ Viz\ Catalog.ipynb --execute --output viz.md
=======
# run the commands below while in the "cuxfilter/notebooks/Additional Visualizations Catalogue" directory
# add embed function to the panel dashboards, to generate an interactive web-page
./update-notebooks.sh

rm -rf state/* && jupyter nbconvert --to html RAPIDS\ Viz\ Catalog-static.ipynb --execute --output index.html
>>>>>>> 1520692538cf556c6833e85856a148e23e819560
```
