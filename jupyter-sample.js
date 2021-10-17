import React from 'react';
import ReactDOM from 'react-dom';
import JupyterViewer from "react-jupyter-notebook";
import nb_test from "./nb_test.json"; // You need to read the .ipynb file into a JSON Object.

ReactDOM.render(
  <React.StrictMode>
    <JupyterViewer rawIpynb={nb_test}/>
  </React.StrictMode>,
  document.getElementById('root')
);