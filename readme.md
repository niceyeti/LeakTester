Monitoring:

	1) Stationary: load a page, periodically record memory usage metrics
		- enable/disable
		- write to disk: {ts, heap size, node count}

	2) Testing:
		Action based:
			- Given: a page/control
			- When: action is taken
			- Then: snapshot metrics before and after 
		
			- Define the target control
			- Define a list of actions
			- Define an interval to execute the actions
			- Record metrics before/after








