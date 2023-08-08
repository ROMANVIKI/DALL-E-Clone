export default {
  server: {
    proxy: {
      '/api': 'http://localhost:8000', // Assuming your Django development server runs on port 8000
    },
  },
};
