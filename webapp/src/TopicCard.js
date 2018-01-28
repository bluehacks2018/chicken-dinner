import React, { Component } from 'react';

class TopicCard extends Component {
	constructor(props){
		super(props);
		this.handleClick = this.handleClick.bind(this);
		this.state = {selected: false, topicsClass:'topics-card'}
	}

	handleClick(e){
		this.setState({
			selected: !this.state.selected, 
			topicsClass: this.state.selected ? "topics-card selected" : "topics-card"
		});
	}

	render() {
		return (
			<div class={this.state.topicsClass} onClick={this.handleClick}>
				{this.props.name}
			</div>
		);
	}
}

export default TopicCard;