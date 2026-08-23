import React, { useEffect, useState } from "react";

function LaborHireModal({

    show,

    labor,

    onClose,

    onConfirm

}) {

    const [startDate, setStartDate] = useState("");

    const [days, setDays] = useState(1);

    const [totalAmount, setTotalAmount] = useState(0);

    useEffect(() => {

        if (labor) {

            setTotalAmount(
                labor.daily_wage * days
            );

        }

    }, [days, labor]);

    if (!show || !labor) return null;

    return (

        <div
            className="modal d-block"
            style={{
                background: "rgba(0,0,0,.5)"
            }}
        >

            <div className="modal-dialog">

                <div className="modal-content">

                    <div className="modal-header">

                        <h5>

                            👷 Hire Labor

                        </h5>

                        <button
                            className="btn-close"
                            onClick={onClose}
                        />

                    </div>

                    <div className="modal-body">

                        <h5>

                            {labor.full_name}

                        </h5>

                        <p>

                            ₹{labor.daily_wage}/day

                        </p>

                        <label>

                            Start Date

                        </label>

                        <input
                            type="date"
                            className="form-control mb-3"
                            value={startDate}
                            onChange={(e)=>
                                setStartDate(e.target.value)
                            }
                        />

                        <label>

                            Number of Days

                        </label>

                        <input
                            type="number"
                            min="1"
                            className="form-control"
                            value={days}
                            onChange={(e)=>
                                setDays(Number(e.target.value))
                            }
                        />

                        <div className="alert alert-success mt-3">

                            <strong>

                                Total :

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
                            disabled={!startDate}
                            onClick={()=>

                                onConfirm({

                                    labor_id: labor.id,

                                    start_date: startDate,

                                    total_amount: totalAmount,

                                    number_of_days: days

                                })

                            }
                        >

                            Hire Now

                        </button>

                    </div>

                </div>

            </div>

        </div>

    );

}

export default LaborHireModal;