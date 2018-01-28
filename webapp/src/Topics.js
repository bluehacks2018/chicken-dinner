import React, { Component } from 'react';
import TopicCard from './TopicCard.js';

class Topics extends Component {
	render() {
		return (
			<div class="topics">
				<div class="topics-container">
					<h1>What do you want to know about?</h1>

					<TopicCard name="Environment" />
					<TopicCard name="Education" />
					<TopicCard name="Justice" />
					<TopicCard name="Health" />
					<TopicCard name="Culture" />
					<TopicCard name="Sports" />
					<TopicCard name="Entertainment" />
					<TopicCard name="Transportation" />
					<TopicCard name="Technology" />
					<TopicCard name="Finance" />

					<a href="/dashboard" class="btn-finish">Finish</a>
				</div>
			</div>
		);
	}
}

export default Topics;