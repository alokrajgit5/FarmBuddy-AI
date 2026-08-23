import React, { useEffect, useState } from "react";

function BookingModal({

  show,

  onClose,

  tractor,

  onConfirm

}) {

  const [startDate, setStartDate] = useState("");

  const [endDate, setEndDate] = useState("");

  const [totalAmount, setTotalAmount] = useState(0);

  useEffect(() => {

    if (
      startDate &&
      endDate &&
      tractor
    ) {

      const start = new Date(startDate);

      const end = new Date(endDate);

      const diffDays = Math.ceil(

        (end - start) /

        (1000 * 60 * 60 * 24)

      ) + 1;

      if (diffDays > 0) {

        setTotalAmount(

          diffDays * tractor.price_per_day

        );

      } else {

        setTotalAmount(0);

      }

    }

  }, [

    startDate,

    endDate,

    tractor

  ]);

  if (!show || !tractor) {

    return null;

  }

  return (

    <div
      className="modal d-block"
      style={{
        background: "rgba(0,0,0,0.5)"
      }}
    >

      <div className="modal-dialog">

        <div className="modal-content">

          <div className="modal-header">

            <h5 className="modal-title">

              🚜 Book Tractor

            </h5>

            <button

              className="btn-close"

              onClick={onClose}

            />

          </div>

          <div className="modal-body">

            <h5>

              {tractor.tractor_name}

            </h5>

            <p>

              ₹{tractor.price_per_day}/day

            </p>

            <div className="mb-3">

              <label>

                Start Date

              </label>

              <input

                type="date"

                className="form-control"

                value={startDate}

                onChange={(e)=>

                  setStartDate(

                    e.target.value

                  )

                }

              />

            </div>

            <div className="mb-3">

              <label>

                End Date

              </label>

              <input

                type="date"

                className="form-control"

                value={endDate}

                onChange={(e)=>

                  setEndDate(

                    e.target.value

                  )

                }

              />

            </div>

            <div className="alert alert-success">

              <strong>

                Total Amount :

              </strong>

              ₹{totalAmount}

            </div>

          </div>

          <div className="modal-footer">

            <button

              className="btn btn-secondary"

              onClick={onClose}

            >

              Cancel

            </button>

            <button

              className="btn btn-success"

              disabled={

                !startDate ||

                !endDate ||

                totalAmount === 0

              }

              onClick={()=>

                onConfirm({

                  tractor_id: tractor.id,

                  start_date: startDate,

                  end_date: endDate,

                  total_amount: totalAmount

                })

              }

            >

              Confirm Booking

            </button>

          </div>

        </div>

      </div>

    </div>

  );

}

export default BookingModal;