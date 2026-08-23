import React, { useEffect, useState } from "react";

function SeedBuyModal({

    show,

    seed,

    onClose,

    onConfirm

}) {

    const [quantity, setQuantity] = useState(1);

    const [purchaseDate, setPurchaseDate] = useState("");

    const [totalPrice, setTotalPrice] = useState(0);

    useEffect(() => {

        if (seed) {

            setTotalPrice(seed.price * quantity);

        }

    }, [seed, quantity]);

    if (!show || !seed) return null;

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

                            🌱 Buy Seed

                        </h5>

                        <button
                            className="btn-close"
                            onClick={onClose}
                        />

                    </div>

                    <div className="modal-body">

                        <h5>

                            {seed.seed_name}

                        </h5>

                        <p>

                            ₹{seed.price} / KG

                        </p>

                        <label>

                            Quantity (KG)

                        </label>

                        <input

                            type="number"

                            min="1"

                            max={seed.quantity}

                            className="form-control mb-3"

                            value={quantity}

                            onChange={(e)=>

                                setQuantity(Number(e.target.value))

                            }

                        />

                        <label>

                            Purchase Date

                        </label>

                        <input

                            type="date"

                            className="form-control mb-3"

                            value={purchaseDate}

                            onChange={(e)=>

                                setPurchaseDate(e.target.value)

                            }

                        />

                        <div className="alert alert-success">

                            <strong>

                                Total Price :

                            </strong>

                            ₹{totalPrice}

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

                            disabled={!purchaseDate}

                            onClick={()=>

                                onConfirm({

                                    seed_id: seed.id,

                                    quantity,

                                    purchase_date: purchaseDate

                                })

                            }

                        >

                            🛒 Buy Now

                        </button>

                    </div>

                </div>

            </div>

        </div>

    );

}

export default SeedBuyModal;