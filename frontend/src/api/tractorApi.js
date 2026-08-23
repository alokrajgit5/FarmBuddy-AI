import api from "./axios";

// Get All Tractors
export const getAllTractors = async () => {
  const response = await api.get("/api/tractors/");
  return response.data;
};

// Get Tractor By ID
export const getTractorById = async (id) => {
  const response = await api.get(`/api/tractors/${id}`);
  return response.data;
};

// Create Tractor
export const createTractor = async (data) => {
  const response = await api.post("/api/tractors/", data);
  return response.data;
};

// Update Tractor
export const updateTractor = async (id, data) => {
  const response = await api.put(`/api/tractors/${id}`, data);
  return response.data;
};

// Delete Tractor
export const deleteTractor = async (id) => {
  const response = await api.delete(`/api/tractors/${id}`);
  return response.data;
};