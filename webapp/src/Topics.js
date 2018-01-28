import React, { Component } from 'react';
import TopicCard from './TopicCard.js';

class Topics extends Component {
	constructor(props){
		super(props);
		this.handlePost = this.handlePost.bind(this);
		this.state = {
			step:1
		}
	}

	handlePost(){
		const url = "http://localhost:8000/user/create/";
		console.log(this.props.data);

		fetch(url, {
			method: 'POST',
			headers: {
				'Accept': 'application/json',
				'Content-Type':'application/json'
			},
			body: JSON.stringify({
				"user": {
					"username": this.props.data.username,
					"first_name": this.props.data.first_name,
					"last_name": this.props.data.last_name,
					"password": this.props.data.password
				},
				"city": this.props.data.city,
				"onboard_answer_1": this.props.data.onboard_answer_1,
				"onboard_answer_2": this.props.data.onboard_answer_2,
				"preferences": [1, 3]
			})
		});
	}

	render() {
		return (
			<div class="topics">
				<div class="topics-container">
					<h1>What do you want to know about?</h1>

					<TopicCard name="Education" />
					<TopicCard name="Government Spending" />
					<TopicCard name="Health" />
					<TopicCard name="Culture" />
					<TopicCard name="Sports" />
					<TopicCard name="Entertainment" />
					<TopicCard name="Transportation" />
					<TopicCard name="Technology" />
					<TopicCard name="Finance" />

					<button href="/dashboard" class="btn-finish" onClick={this.handlePost} >Finish</button>
				</div>
			</div>
		);
	}
}

export default Topics;