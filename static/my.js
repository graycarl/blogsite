function set_selected(name)
{
	var sname = "nav_" + name
	var selement = document.getElementById(sname)
	if (selement)
	{
		selement.className = "nav_selected"
	}
}
