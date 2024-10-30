from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing_extensions import Annotated
from typing import List

app = FastAPI()

class ProductSales(BaseModel):
	productId: str
	sales: float

class ProductStock(BaseModel):
	productId: str
	stock: int

class Item(BaseModel):
	salesWeight: Annotated[float, Query(ge=0, le=1)]
	stockWeight: Annotated[float, Query(ge=0, le=1)]
	productSales: List[ProductSales]
	productStock: List[ProductStock]

@app.get("/")
def read_root():
	return "Hello world"
	
def get_weight(salesWeight:float, stockWeight: float, sales: int, stock: int):
	return sales * salesWeight + stock * stockWeight
	
@app.post("/sort-products")
def sort_products(item: Item):
	list_products = []
	result= []
	
	if item.salesWeight + item.stockWeight <=1:
		for i in item.productSales:
			for j in item.productStock:
				if i.productId == j.productId:
					weight = get_weight(item.salesWeight, item.stockWeight, i.sales, j.stock)
					product = (i.productId, weight)
					list_products.append(product)
	
		list_products.sort(key= lambda x: x[1], reverse= True)
		
		for i in list_products:
			result.append(i[0])
	else:
		result.append("Las ponderaciones deben sumar 1 en total")
			
	return result
		

		
		
		
		
		
		
		
		
		
