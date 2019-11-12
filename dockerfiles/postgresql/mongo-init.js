db.createUser(
{
	user:"modana",
	pwd:"creditScore",
	roles:[
			{
				role:"readWrite", db:"CreditScoreEngine_dev"
		}
	]
})