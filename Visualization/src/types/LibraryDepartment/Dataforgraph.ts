
export interface Dataforgraph{
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
	/**	Car Name : Data	*/
	car_name?: string
	/**	Year : Int	*/
	year?: number
	/**	Selling Price : Currency	*/
	selling_price?: number
	/**	Present Price : Currency	*/
	present_price?: number
	/**	Kms Driven : Float	*/
	kms_driven?: number
	/**	Fuel Type : Select	*/
	fuel_type?: "Petrol" | "Diesel" | "CNG"
	/**	Seller Type : Select	*/
	seller_type?: "Dealer" | "Indivisual"
	/**	Transmission : Select	*/
	transmission?: "Manual" | "Automatic"
	/**	Owners : Select	*/
	owners?: "Single" | "Second" | "Third" | "Fourth" | "Fifth"
}