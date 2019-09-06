import React, { Component } from "react";
import { UncontrolledCollapse} from 'reactstrap';
import Moment from 'react-moment';
import Modal from "./components/Modal";
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      viewCompleted: false,
      activeItem: {
        title: "",
        description: "",
        completed: false,
        createdDate: "",
      },
      todoList: [],
    };
  }

  componentDidMount() {
    this.refreshList();
  }
  refreshList = () => {
    axios
      .get("http://localhost:8000/api/todos/")
      .then(res => this.setState({ todoList: res.data }))
      .catch(err => console.log(err));
  };


  renderItems = () => {
    const newItems = this.state.todoList;
    return newItems.map(item => (
      <li
        key={item.id}
        className="list-group-item d-flex list-group-item-action justify-content-between align-items-center"
      >
        <span
          className={`todo-title mr-2 ${
            item.completed ? "completed-todo" : ""
          }`}
        >
          {item.title}
          <UncontrolledCollapse toggler="#toggler">
            <div className="card">
              <div className="card-title m-3 font-italic">Created Date: <Moment format="YYYY/MM/DD--HH:MM">{item.createdDate}</Moment></div>
              <div className="card-body m-0">{item.description}</div>
            </div>
          </UncontrolledCollapse>
        </span>

        <span className="row">
          <button
            onClick={() => this.editItem(item)}
            className="btn btn-light font-weight-light mr-2"
          >
            Edit
          </button>
          <button
            onClick={() => this.handleDelete(item)}
            className="btn btn-dark font-weight-light"
          >
            Delete
          </button>
        </span>
      </li>
    ));
  };
  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };
  handleSubmit = item => {
    this.toggle();
    if (item.id) {
      axios
        .put(`http://localhost:8000/api/todos/${item.id}/`, item)
        .then(res => this.refreshList());
      return;
    }
    axios
      .post("http://localhost:8000/api/todos/", item)
      .then(res => this.refreshList());
  };
  handleDelete = item => {
    axios
      .delete(`http://localhost:8000/api/todos/${item.id}/`)
      .then(res => this.refreshList());
  };
  createItem = () => {
    const item = { title: "", description: "", completed: false, createdDate: "" };
    this.setState({ activeItem: item, modal: !this.state.modal });
  };
  editItem = item => {
    this.setState({ activeItem: item, modal: !this.state.modal });
  };
  render() {
    return (
      <main className="content">
        <h1 className="text-dark text-center my-5">Pre Work</h1>
        <div className="row ">
          <div className="col-lg-5 col-sm-10 mx-auto">
            <div className="card">
              <img className="img-fluid" src={"/todolist.png"} alt={"test"} />
              <div className="row m-3 my-3">
                <button onClick={this.createItem} className="btn btn-light btn-lg font-weight-light">
                  Add task
                </button>
                <button className="btn btn-light btn-lg mx-3 font-weight-light" id="toggler">
                  Show detail
                </button>
              </div>
              <ul className="list-group list-group-flush">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
        {this.state.modal ? (
          <Modal
            activeItem={this.state.activeItem}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}
      </main>
    );
  }
}
export default App;