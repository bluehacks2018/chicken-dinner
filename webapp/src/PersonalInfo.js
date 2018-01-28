import React, { Component } from 'react';

import Topics from './Topics';

class PersonalInfo extends Component {
	constructor(props){
		super(props);
		this.handleChange = this.handleChange.bind(this);
		this.handleClick = this.handleClick.bind(this);
		this.state = {
			step: 1,
			username: null,
			first_name: null,
			last_name: null,
			password: null,
			city: null,
			onboard_answer_1: null,
			onboard_answer_2: null
		}
	}

	handleClick(e){
		e.preventDefault();
		this.setState({
			step: this.state.step + 1
		});
		console.log(this.state.step)

	}

	handleChange(e){
		const state_name = e.target.name;
		const state_value = e.target.value;
		this.setState({ [state_name] : state_value });
		console.log(this.state);
	}

	render() {
		switch(this.state.step){
			case 1:
				return (
					<div class="personal">
						<div class="personal-container">
							<h1>Tell us about yourself.</h1>
							<form>
								<div class="field">
									<label>Username:</label>
									<input type="text" name="username" onChange={this.handleChange}/>
								</div>
								<div class="field">
									<label>First Name:</label>
									<input type="text" name="first_name" onChange={this.handleChange}/>
								</div>
								<div class="field">
									<label>Last Name:</label>
									<input type="text" name="last_name" onChange={this.handleChange}/>
								</div>
								<div class="field">
									<label>Password:</label>
									<input type="password" name="password" onChange={this.handleChange}/>
								</div>
								<div class="field">
									<label>Age:</label>
									<input type="text" name="age" />
								</div>
								<div class="field">
									<label> City:</label>
									<input type="text" name="city" onChange={this.handleChange}/>
								</div>

								<div class="field">
									<label >School/Employer:</label>
									<input type="text" name="school-employer" onChange={this.handleChange}/>
								</div>
								
								<div class="field">
									<label> What do you care about?</label>
									<textarea rows="4" name="onboard_answer_1" onChange={this.handleChange}/>
								</div>

								<div class="field">
									<label> What do you envision for the Philippines?</label>
									<textarea rows="4" name="onboard_answer_2" onChange={this.handleChange}/>
								</div>
								<center><input class="btn-next" value="Next" onClick={this.handleClick}/></center>
							</form>
						</div>
					</div>
				);
			case 2: 
				return <Topics data={this.state} />
		}
	}
}

export default PersonalInfo;