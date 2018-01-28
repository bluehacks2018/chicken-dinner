import React, { Component } from 'react';
import Pie from './Pie';

class DashboardCard extends Component {
	constructor(props){
		super(props);
	}

	render() {
		return (
			<div>
				<div class="dashboard-card">
					<div class="topic-category">{this.props.tag}</div>
					<div class="topic-details">
						<h1>{this.props.name}</h1>
						<h2>{this.props.gov_org}</h2>
						<p>{this.props.desc}</p>
					</div>
					<div class="topic-viz"> 
						<Pie data={this.props.data} chart_type={this.props.chart_type}/>
					</div>
				</div>
			</div>
		);
	}
}

export default DashboardCard;