var mongoose = require('mongoose');
const { options } = require('.');

// note: your host/port number may be different!
mongoose.connect(`mongodb+srv://sandesh:${process.env.DBPASSWORD}@mongo-aws.bav9k.mongodb.net/myDb?retryWrites=true&w=majority`,{useNewUrlParser: true})
.catch(e=>console.log(e))


var Schema = mongoose.Schema;

var animalSchema = new Schema( {
	name: {type: String, required: true, unique: true},
	species: {type: String, required: true},
	breed: String,
	gender: {type: String, enum: ['male', 'female']},
	traits: [String],
	age: Number
    } );


module.exports = mongoose.model('Animal', animalSchema);
