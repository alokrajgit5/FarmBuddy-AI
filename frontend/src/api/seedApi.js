import api from "./axios";

// Get All Seeds
export const getAllSeeds = async () => {

    const response = await api.get("/api/seeds/");

    return response.data;

};

// Get Seed By ID
export const getSeedById = async (id) => {

    const response = await api.get(`/api/seeds/${id}`);

    return response.data;

};

// Create Seed
export const createSeed = async (data) => {

    const response = await api.post("/api/seeds/", data);

    return response.data;

};

// Update Seed
export const updateSeed = async (id, data) => {

    const response = await api.put(`/api/seeds/${id}`, data);

    return response.data;

};

// Delete Seed
export const deleteSeed = async (id) => {

    const response = await api.delete(`/api/seeds/${id}`);

    return response.data;

};