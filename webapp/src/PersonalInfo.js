import React, { Component } from 'react';

class PersonalInfo extends Component {
	render() {
		return (
			<div class="personal">
				<div class="personal-container">
					<h1>Tell us about yourself.</h1>
					<form>
						<div class="field">
							<label>Name:</label>
							<input type="text" name="name" />
						</div>
						<div class="field">
							<label>Age:</label>
							<input type="text" name="age" />
						</div>
						<div class="field">
							<label> City:</label>
							<input type="text" name="city" />
						</div>

						<div class="field">
							<label >School/Employer:</label>
							<input type="text" name="school-employer" />
						</div>
						
						<div class="field">
							<label> What do you care about?</label>
							<textarea rows="4" name="what-care" />
						</div>

						<div class="field">
							<label> What do you envision for the Philippines?</label>
							<textarea rows="4" name="what-care" />
						</div>
						<center><a href="/topics" class="btn-next">Next</a></center>
					</form>
				</div>
			</div>
		);
	}
}

export default PersonalInfo;