require('dotenv').config();
var express = require('express');
var app = express();

var Animal = require('./Animal.js');
var Toy = require('./Toy.js');


app.use('/findToy', async (req,res) => {
    const toyId = req.query.id;

    if (!toyId){
        res.json({});
    }else{
        const response = await Toy.findOne({id: toyId});
        response? res.json(response): res.json({});
    }
})

app.use('/findAnimals', async (req,res) => {

    if(!req.query.species && !req.query.gender && !req.query.trait) res.json({});

    let query = {};
    if (req.query.species) query.species = req.query.species;
    if (req.query.gender) query.gender = req.query.gender;

    let result = await Animal.find(query);
    if (req.query.trait) result = result.filter(animal =>  animal.traits.includes(req.query.trait));
    const response = result.map(animal => {
        return {
            name: animal.name,
            species: animal.species,
            age: animal.age,
            breed: animal.breed,
            gender: animal.gender,
        }
    })
    response.length > 0? res.send(response):res.json({});
})

app.use('/animalsYoungerThan', async (req,res) => {
    if (!req.query.age) res.json({})

    try{
        let result = await Animal.find({age: {$lt:req.query.age}});
        const count = result.length;
        if (!count) res.json({count: 0})
        const names = result.map(animal => animal.name);

        res.json({count,names});
    }
    catch(err){
        console.log(err);
        res.json({})
    }

})

app.use('/calculatePrice', async (req,res) => {
    
    if (!req.query.id || !req.query.qty) res.json({})
    if (req.query.id.length != req.query.qty.length) res.json({})
    try{
        const idQueries = req.query.id.map(id=> {return {id: id}});
        const response = await Toy.find({$or: [...idQueries]})
        let items = []
        let totalPrice = 0;
        response.forEach(item => {
            let newItem = {}
            const idx = req.query.id.indexOf(item.id);
            const qty = req.query.qty[idx];
            if (idx >=0 && qty!=null && Number.isInteger(Number(qty)) && Number(qty)>0 ){
                newItem.item = item.id;
                newItem.qty = qty;
                newItem.subtotal = item.price * Number(qty);
                totalPrice += item.price * Number(qty);
                items.push(newItem);
            }
        })
        res.json({
            totalPrice,
            items
        })
    }
    catch(e){
        res.json({});
    }

})

app.use('/', (req, res) => {
	res.json({ msg : 'It works!' });
    });



app.listen(3000, () => {console.log('Listening on port 3000');});


// Please do not delete the following line; we need it for testing!
module.exports = app;