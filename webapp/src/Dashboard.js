import React, { Component } from 'react';
import sampleData from './sample-input.json';

import DashboardCard from './DashboardCard';

class Dashboard extends Component {
	constructor(props){
		super(props);
	}
	
	render() {
		return (
			<div class="dashboard">
				<div class="dashboard-container">
					<h1>Dashboard</h1>
					<DashboardCard 
						name={sampleData.name} 
						gov_org={sampleData.gov_org} 
						desc={sampleData.description} 
						tag={sampleData.tag} 
						chart_type={sampleData.chart_type} 
						data={sampleData.data} />
				</div>
			</div>
		);
	}
}

export default Dashboard;