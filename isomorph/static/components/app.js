var React = require('react');

var App = React.createClass({displayName: "App",
  render: function(){
    console.log("I am here...");
    return (
      React.createElement('span', null, "I'm a react component")
    );
  }
});

module.exports = App;
