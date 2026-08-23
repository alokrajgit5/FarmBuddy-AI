import Sidebar from "../components/Sidebar";
import RightSidebar from "../components/RightSidebar";

function DashboardLayout({ children, dashboard }) {

  return (

    <div
      style={{
        display: "flex",
        background: "#F5F7F2",
        minHeight: "100vh"
      }}
    >

      <Sidebar />

      <main
        style={{
          flex: 1,
          padding: "30px"
        }}
      >
        {children}
      </main>

      <RightSidebar dashboard={dashboard} />

    </div>

  );

}

export default DashboardLayout;