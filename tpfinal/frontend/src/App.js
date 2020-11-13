import './App.css';
import React from "react";
import {BrowserRouter, Route, Switch} from "react-router-dom";
import Homepage from "./pages/homepage/Homepage";

function App() {
  return (
      <BrowserRouter>
          <Switch>
              <Route exact
                     path="/"
                     render={() => <Homepage/>}></Route>
          </Switch>
      </BrowserRouter>
  );
}

export default App;
