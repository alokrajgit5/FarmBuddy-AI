import { CircularProgressbar } from "react-circular-progressbar";
import "react-circular-progressbar/dist/styles.css";

export default function CropHealthCard({ dashboard }) {

    return (

        <div className="bg-white rounded-2xl shadow-lg p-6">

            <h2 className="text-xl font-bold mb-5">

                Crop Health

            </h2>

            <div className="w-44 h-44 mx-auto">

                <CircularProgressbar
                    value={dashboard.crop_health_score}
                    text={`${dashboard.crop_health_score}%`}
                    styles={{
                        path: {
                            stroke:
                                dashboard.crop_health_score >= 90
                                    ? "#16a34a"
                                    : dashboard.crop_health_score >= 75
                                    ? "#eab308"
                                    : "#dc2626"
                        },
                        text: {
                            fill: "#111827",
                            fontSize: "18px"
                        },
                        trail: {
                            stroke: "#e5e7eb"
                        }
                    }}
                />

                

            </div>

            <h3 className="text-center mt-5 text-xl font-bold text-green-600">

                {dashboard.crop_health_status}

            </h3>

            <p className="text-center text-gray-500 mt-2">

                Disease Risk :

                <span className="font-semibold">

                    {" "}
                    {dashboard.disease_risk}

                </span>

            </p>

            <div className="mt-5 bg-green-50 p-4 rounded-xl">

                <p className="font-semibold">

                    AI Recommendation

                </p>

                <p className="text-gray-600 mt-2">

                    {dashboard.crop_recommendation}

                </p>

            </div>

        </div>

    );

}