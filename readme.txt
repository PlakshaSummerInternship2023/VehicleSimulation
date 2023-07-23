class Body:
	"""
	depicts a body, which can move in a given dimensional space,
	"""
	instance variables:
		int dimension :
			- basically tells if the object is 2 or 3 dimensional
		np.ndarray vertices   :
			- shape (None, dimension) , dtype=np.float32
			- contains points which correlate to the shape of
			  the vehicle
			- if the value is None it means that the shape is
			  a point object
		np.ndarray edges :
			- shape (None, 2) , dtype=np.float32
			- contains all the vertices which are connected
		np.ndarray center_of_mass :
			- shape (dimension, ), dtype=np.float32
			- the location of the center of mass
		PhysicsAttrbutes phys_attributes :
			- contains all the attributes pertaining to the orientation
			  of the vehicle
		list[Engine] engines :
			- it creates a list of all engine objects

	functions :
		def physics_process (delta : np.float32, forces : list[dict]) -> EngineResponse():
			- delta is the difference in time between subsequent calls
			- forces is a list of dictionaries, containing information regarding
			  the location and the magnitude of the forces
			- will return and EngineResponse which will subsequently tell the engine
			  where and how to move
			- will operate mainly through private methods
		def show () -> None:
			- draws the body once to check if the envisioned architecture is the
			  same as the one envisioned
		@classmethod
		def from_config(fname : str) -> Body :
			- creates the object from a configuration file, the spec will be like .object files of blender
		

class PhysicsAttributes:
	"""
	Basically contains all the physical attributes related to any object which might need it
	"""
	instance variables:
		int dimension :
			- basically tells if the object is 2 or 3 dimensional
		np.float32 mass:
			- depicts the mass of the body
			- is taken as 1.0 if the value is None
		np.float32 scale :
			- tells how much should the vehicle be scaled up to
		np.ndarray destination :
			- shape (dimension, ), dtype=np.float32
			- the location where the body has to reach in the global scope
		np.ndarray location:
			- shape (dimension,), dtype=np.float32,
			- tells the location of the object in global scope, on the plot
		np.ndarray rotation:
			- shape (dimension+1, ), dtype=np.float32,
			- tells us about the rotation of the object
			- dimension+1 is used as 2d rotation has a 3d rotation vector
			  and 3d rotation is often simplified by quaternions

		
		np.ndarray net_momentum:
			- shape (dimension, ), dtype=np.float32
			- tells us of about the net momentum of a body (from the center of mass)
		np.ndarray net_angular_momentum:
			- shape (dimension+1, ), dtype=np.float32
			- tells us about the angular momentum acting on the body (from the center of mass)

		np.ndarray net_force:
			- shape (dimension, ), dtype=np.float32
			- tells us of about the net force of a body (from the center of mass)
		np.ndarray net_torque:
			- shape (dimension+1, ), dtype=np.float32
			- tells us about the net torque acting on the body (from the center of mass)
		
		list[dict] raw_momentum:
			- each index contains a dict for the location & magnitude of the momentum
			- dtype=np.float32,
			- this field is optional in case it is needed for debugging
			  or to calculate angular momentum
		list[dict] raw_forces:
			- each index contains a dict for the location & magnitude of the force
			- dtype=np.float32,
			- this field is optional in case it is needed for debugging
			  or to calculate torque

	functions:
		- will be designed based on how we solve the problem

class Thruster:
	instance variables:
		int        dimension :
			- basically tells if the object is 2 or 3 dimensional
		np.ndarray direction :
			- shape (None, dimension), dtype=np.float32
			- contains the directions in which the engine can thrust
		np.ndarray thrust     : 
			- shape (None,2), dtype=np.float32,
			- [1500,1900] pwm
			- contains the value of thrust in newtons (feasable?)
			- each row contains the [pwm, thrust] data
		np.ndarray locations  : 
			- shape (None, dimension) , dtype=np.float32)
			- contains the locations at which each of the engine exists
			- these locations are in local scope
	functions:
		- will be designed based on how we solve the problem
	
class EngineResponse:
	"""
	A response object which contains instructions for the actual vehicle
	"""
	# implemented on the basis of the needs

