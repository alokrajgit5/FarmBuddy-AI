import "./ProfileCompletion.css";

function ProfileCompletion({ profile }) {

  const fields = [

    "phone",
    "state",
    "district",
    "village",
    "land_area",
    "soil_type",
    "main_crop",
    "irrigation",
    "experience",
    "bio"

  ];

  const completed = fields.filter(

    (field) =>

      profile[field] !== null &&
      profile[field] !== "" &&
      profile[field] !== undefined

  ).length;

  const percentage = Math.round(

    (completed / fields.length) * 100

  );

  return (

    <div className="profile-completion-card">

      <div className="d-flex justify-content-between">

        <h4>
          🌱 Profile Completion
        </h4>

        <span className="fw-bold">

          {percentage}%

        </span>

      </div>

      <div className="progress mt-3">

        <div

          className="progress-bar progress-bar-striped progress-bar-animated bg-success"

          role="progressbar"

          style={{

            width: `${percentage}%`

          }}

        >

          {percentage}%

        </div>

      </div>

      <p className="mt-3 text-muted">

        Complete your profile to unlock all FarmBuddy AI features.

      </p>

    </div>

  );

}

export default ProfileCompletion;