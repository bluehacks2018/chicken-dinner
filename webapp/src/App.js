import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link, Switch } from 'react-router-dom'

import Welcome from './Welcome';
import PersonalInfo from './PersonalInfo';
import Topics from './Topics';
import Dashboard from './Dashboard';
import Search from './Search'

import './chartist.css';
import './index.css';

class App extends Component {
	render() {
		return (
			<Router>
				<div>
					<div id="navbar">
						<div class="regular-nav">
							<ul>
								<li><CustomLink to="/search" label="Search"/></li>
								<li><CustomLink to="/dashboard" label="Dashboard"/></li>
							</ul>
						</div>
					</div>

					<Switch>
						<Route exact path="/" component={Welcome}/>
						<Route path="/personalinfo" component={PersonalInfo}/>
						<Route path="/topics" component={Topics}/>
						<Route path="/dashboard" component={Dashboard}/>
						<Route path="/search" component={Search}/>

					</Switch>
				</div>
			</Router>
		);
	}
}

const CustomLink = ({ label, to, activeOnlyWhenExact }) => (
	<Route path={to} exact={activeOnlyWhenExact} children={({ match }) => (
		<Link className={match ? 'active' : ''}to={to}>{label}</Link>
	)}/>
)


export default App;
