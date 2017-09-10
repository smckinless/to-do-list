import React from 'react';

export default class NewTask extends React.Component {

    constructor() {
        super();
        this.state = {showInput:false};
        this.addTask = this.addTask.bind(this);
        this.submitTask = this.submitTask.bind(this);
        this.collapseInput = this.collapseInput.bind(this);
    }

    addTask() {
        /* $.ajax({
            url: 'api/v1/task/add/',
            data:
        }); */

        this.setState({showInput:true});
    }

    submitTask(e) {
        event.preventDefault();
        var data = {'name': e.target.name.value};
        $.ajax({
            url: '/api/v1/task/create/',
            data: data,
            datatype: 'json',
            type: 'POST',
            success: function(data) {
                alert('New task added');
            },
            error: function(error) {
                console.log(error);
            }
        });
    }

    collapseInput() {
        this.setState({showInput:false});
    }

    render() {
        if (this.state.showInput) {
            var task = (
                <div>
                    <div className='task-title'>
                        New Task
                    </div>
                    <span className="glyphicon glyphicon-minus task-glyph" aria-hidden="true" onClick={this.collapseInput} />
                    <form onSubmit={this.submitTask}>
                        <input name='name' type='text' />
                        <input type='submit' value='Submit' />
                    </form>
                </div>
            );
        } else {
            var task = (
                <div>
                    <div className='task-title'>
                        New Task
                    </div>
                    <span className="glyphicon glyphicon-plus task-glyph" aria-hidden="true" onClick={this.addTask} />
                </div>
            );
        }
        return (
            <li className='newTask'>
                {task}
            </li>
        );
    }
}