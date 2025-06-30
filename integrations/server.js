const fastify = require('fastify')({ logger: true });
const axios = require('axios');
const cors = require('@fastify/cors');

fastify.register(cors, {
  origin: '*',
  methods: ['GET']
});

fastify.get('/', async (req, reply) => {
  reply.send({ message: 'Flight proxy is alive' });
});

fastify.get('/get', async (req, reply) => {
  const { flightNumber, flightDate } = req.query;

  if (!flightNumber || !flightDate) {
    return reply.status(400).send({ error: 'Missing flightNumber or flightDate' });
  }

  try {
    const res = await axios.get(`https://aerodatabox.p.rapidapi.com/flights/number/${flightNumber}/${flightDate}`, {
      headers: {
        'X-RapidAPI-Key': '330a15767bmsh691f47052120171p1a403fjsndbc649167a5e',
        'X-RapidAPI-Host': 'aerodatabox.p.rapidapi.com'
      }
    });

    reply.send(res.data);
  } catch (err) {
    reply.status(500).send({ error: err.response?.data || err.message });
  }
});

const start = async () => {
  try {
    await fastify.listen({ port: process.env.PORT || 3000, host: '0.0.0.0' });
  } catch (err) {
    fastify.log.error(err);
    process.exit(1);
  }
};

start();
