import React, { Component } from 'react';

class Welcome extends Component {
	constructor(props){
		super(props);
	}

	render() {
		return (
			<div class="welcome">
				<div class="welcome-container">
					<h1>Saga</h1>
					<p>Data redefined.</p>
					<a href="/personalinfo" class="btn-start">Start</a>
				</div>
			</div>
		);
	}
}

export default Welcome;