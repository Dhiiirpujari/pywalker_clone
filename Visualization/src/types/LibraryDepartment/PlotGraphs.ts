
export interface PlotGraphs{
	creation: string
	name: string
	modified: string
	owner: string
	modified_by: string
	docstatus: 0 | 1 | 2
	parent?: string
	parentfield?: string
	parenttype?: string
	idx?: number
	/**	Document : Link - DocType	*/
	document?: string
	/**	X axis : Select	*/
	x_axis?: string
	/**	Y axis : Select	*/
	y_axis?: string
	/**	Graph Type : Select	*/
	graph_type?: "scatter plots" | "line plots" | "bar plots" | "area plots"
	/**	Second Document : Link - DocType	*/
	second_document?: string
	/**	X axis second : Select	*/
	x_axis_second?: string
	/**	y axis second : Select	*/
	y_axis_second?: string
}