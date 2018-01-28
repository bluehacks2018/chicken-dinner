import React, { Component } from 'react';
import sampleData from './sample-input.json';

import DashboardCard from './DashboardCard';

class Dashboard extends Component {
	constructor(props){
		super(props);
		this.state = {
	      error: null,
	      isLoaded: false,
	      data: null
	    };
	}

	componentDidMount() {
		const url = "http://localhost:8000/dataset/datasets/";

		fetch(url) 
			.then(res => res.json())
		      .then(
		        (result) => {
		          this.setState({
		            isLoaded: true,
		            data: result
		          })

		          console.log(this.state.data)
		        },
		        (error) => {
		          this.setState({
		            isLoaded: true,
		            error
		          });
		        }
		      )

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

					<DashboardCard 
						name={sampleData.name} 
						gov_org={sampleData.gov_org} 
						desc={sampleData.description} 
						tag={sampleData.tag} 
						chart_type={sampleData.chart_type} 
						data={sampleData.data} />
						
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