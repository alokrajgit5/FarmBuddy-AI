import { BrowserRouter, Routes, Route } from "react-router-dom";

import Navbar from "../components/Navbar";

import Dashboard from "../pages/Dashboard";
import Login from "../pages/Login";
import Register from "../pages/Register";
import Profile from "../pages/Profile";
import Weather from "../pages/Weather";
import Chat from "../pages/Chat";
import Tractor from "../pages/Tractor";
import Labor from "../pages/Labor";
import SeedMarketplace from "../pages/SeedMarketplace";
import MySeedPurchases from "../pages/MySeedPurchases";
import MyLaborBookings from "../pages/MyLaborBookings";
import MyTractorBookings from "../pages/MyTractorBookings";
import VoiceAssistant from "../pages/VoiceAssistant";
import NotFound from "../pages/NotFound";

function AppRoutes() {

  return (

    <BrowserRouter>

      <Navbar />

      <Routes>

        <Route path="/" element={<Dashboard />} />

        <Route path="/login" element={<Login />} />

        <Route path="/register" element={<Register />} />

        <Route path="/profile" element={<Profile />} />

        <Route path="/weather" element={<Weather />} />

        <Route path="/chat" element={<Chat />} />

        <Route path="/tractors" element={<Tractor />} />

        <Route path="/my-tractor-bookings" element={<MyTractorBookings />} />

        <Route path="/labors" element={<Labor />} />

        <Route path="/my-labor-bookings" element={<MyLaborBookings />} />

        <Route path="/seeds" element={<SeedMarketplace />} />

        <Route path="/my-seed-purchases" element={<MySeedPurchases />} />

        <Route path="/voice" element={<VoiceAssistant />} />

        <Route path="*" element={<NotFound />} />

      </Routes>

    </BrowserRouter>

  );

}

export default AppRoutes;