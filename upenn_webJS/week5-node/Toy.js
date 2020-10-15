var mongoose = require('mongoose');

// note: your host/port number may be different!

mongoose.connect(`mongodb+srv://sandesh:${process.env.DBPASSWORD}@mongo-aws.bav9k.mongodb.net/myDb?retryWrites=true&w=majority`,{useNewUrlParser: true})
.catch(e=>console.log(e))

var Schema = mongoose.Schema;

var toySchema = new Schema( {
	id: {type: String, required: true, unique: true},
	name: {type: String, required: true},
	price: Number
    } );


module.exports = mongoose.model('Toy', toySchema);
