// App.jsx
import React from "react";
import Hello from "./Hello";
import { PageHeader } from "react-bootstrap";

export default class App extends React.Component {
  render () {
    return (
      <PageHeader>
        <div className='header-contents'>
          <Hello name='Allyn' />
        </div>
      </PageHeader>
    );
  }
}