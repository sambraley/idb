class NavBar extends React.Component { 
	render() {
		return (
				<nav className="navbar navbar-default navbar-fixed-top" role="navigation">
			      <div className="container">
			        <div className="navbar-header">
			          <a className="navbar-brand active" href="/">SpaceCowboys</a>
			        </div>
			        <div className="collapse navbar-collapse">
			          <ul className="nav navbar-nav">
			            <li><a className="navbar-item" href="/planetoids">Planetoids</a></li>
			            <li><a className="navbar-item" href="/galaxies">Galaxies</a></li>
			            <li><a className="navbar-item" href="/satellites">Satellites</a></li>
			            <li><a className="navbar-item" href="/stars">Stars</a></li>  
			            <li><a className="navbar-item" href="/about">About</a></li> 
			            <li><a className="navbar-item" href="/report">Report</a></li>    
			          </ul>
			        </div>
			      </div>
			    </nav>
			);
	}
}


export default NavBar;