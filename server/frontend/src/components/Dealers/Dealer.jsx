import React, { useState,useEffect } from 'react';
import { useParams } from 'react-router-dom';
import "./Dealers.css";
import "../assets/style.css";
import positive_icon from "../assets/positive.png"
import neutral_icon from "../assets/neutral.png"
import negative_icon from "../assets/negative.png"
import review_icon from "../assets/reviewbutton.png"
import Header from '../Header/Header';

const Dealer = () => {


  const [dealer, setDealer] = useState({});
  const [reviews, setReviews] = useState([]);
  const [unreviewed, setUnreviewed] = useState(false);
  const [postReview, setPostReview] = useState(<></>)

  let curr_url = window.location.href;
  let root_url = curr_url.substring(0,curr_url.indexOf("dealer"));
  let params = useParams();
  let id =params.id;
  let dealer_url = root_url+`djangoapp/dealer/${id}`;
  let reviews_url = root_url+`djangoapp/reviews/dealer/${id}`;
  let post_review = root_url+`postreview/${id}`;
  
  const get_dealer = async ()=>{
    const res = await fetch(dealer_url, {
      method: "GET"
    });
    const retobj = await res.json();
    
    if(retobj.status === 200) {
      let dealerobjs = Array.from(retobj.dealer)
      setDealer(dealerobjs[0])
    }
  }

  const get_reviews = async ()=>{
    const res = await fetch(reviews_url, {
      method: "GET"
    });
    const retobj = await res.json();
    
    if(retobj.status === 200) {
      if(retobj.reviews.length > 0){
        setReviews(retobj.reviews)
      } else {
        setUnreviewed(true);
      }
    }
  }

  const senti_icon = (sentiment)=>{
    let icon = sentiment === "positive"?positive_icon:sentiment==="negative"?negative_icon:neutral_icon;
    return icon;
  }

  useEffect(() => {
    get_dealer();
    get_reviews();
    if(sessionStorage.getItem("username")) {
      setPostReview(<a href={post_review}><img src={review_icon} style={{width:'10%',marginLeft:'10px',marginTop:'10px'}} alt='Post Review'/></a>)

      
    }
  // eslint-disable-next-line react-hooks/exhaustive-deps
  },[]);  


return(
  <div style={{margin:"20px"}}>
      <Header/>
      <div style={{marginTop:"10px"}}>
      <h1 style={{color:"grey"}}>{dealer.full_name}{postReview}</h1>
      </div>

      <div className="dealer_details" style={{border:"1px solid #ccc", borderRadius:"6px",
        padding:"12px 16px", maxWidth:"760px", marginBottom:"18px", background:"#fafafa"}}>
        <h3 style={{marginTop:"0", marginBottom:"10px", color:"#333"}}>Dealer details</h3>
        <table className="table" style={{marginBottom:"0"}}>
          <tbody>
            <tr><th style={{width:"28%"}}>Dealer name</th><td>{dealer.full_name}</td></tr>
            <tr><th>Address</th><td>{dealer.address}</td></tr>
            <tr><th>City</th><td>{dealer.city}</td></tr>
            <tr><th>State</th><td>{dealer.state}</td></tr>
            <tr><th>Zip</th><td>{dealer.zip}</td></tr>
            <tr><th>Dealer ID</th><td>{dealer.id}</td></tr>
          </tbody>
        </table>
      </div>

      <h3 style={{color:"#333", marginBottom:"10px"}}>Customer reviews ({reviews.length})</h3>
      <div class="reviews_panel">
      {reviews.length === 0 && unreviewed === false ? (
        <text>Loading Reviews....</text>
      ):  unreviewed === true? <div>No reviews yet! </div> :
      reviews.map(review => (
        <div className='review_panel'>
          <img src={senti_icon(review.sentiment)} className="emotion_icon" alt='Sentiment'/>
          <div className='review'>{review.review}</div>
          <div className="reviewer">{review.name} {review.car_make} {review.car_model} {review.car_year}</div>
        </div>
      ))}
    </div>  
  </div>
)
}

export default Dealer
