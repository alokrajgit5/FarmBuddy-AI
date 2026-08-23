import api from "./axios";

// Get All Labors
export const getAllLabors = async () => {
  const response = await api.get("/api/labors/");
  return response.data;
};

// Get Labor By ID
export const getLaborById = async (id) => {
  const response = await api.get(`/api/labors/${id}`);
  return response.data;
};

// Create Labor
export const createLabor = async (data) => {
  const response = await api.post("/api/labors/", data);
  return response.data;
};

// Update Labor
export const updateLabor = async (id, data) => {
  const response = await api.put(`/api/labors/${id}`, data);
  return response.data;
};

// Delete Labor
export const deleteLabor = async (id) => {
  const response = await api.delete(`/api/labors/${id}`);
  return response.data;
};