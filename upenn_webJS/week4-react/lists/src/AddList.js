import React, { Component } from 'react';

class AddList extends Component {

  constructor() {
    super();
    this.state = {
      newList:{}
    }
  }

  handleSubmit(e) {
      e.preventDefault(); // this prevents the page from reloading -- do not delete this line!

      let newList ={}
      const newListName = this.refs.id.value;
      newList[newListName] = [];
      this.setState({newList: newList},() => {this.props.addList(this.state);})
  
  }

  render() {
    return (
      <div id="addListDiv">
      <form onSubmit={this.handleSubmit.bind(this)}>
      <div id='addList'>
      <label>What will be on your next list?&nbsp;
      <input type='text' ref='id' id='newID'></input>
      </label>
      </div><br />
      <input type='submit' value='Create List' />
      </form>
      </div>
    );
  }
}

export default AddList;
