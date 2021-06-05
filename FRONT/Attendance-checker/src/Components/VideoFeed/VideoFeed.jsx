import React from 'react';
import styled from 'styled-components'

const VideoFeed = () => {
    const VideoFeedSection = styled.section`
        display: flex;
        flex-direction: column;
        margin: 40px 10px;
        background-color: #ffffff;
        padding: 20px;
        width: 45vw;
        h2 {
            margin-top : 0;
            font-size: 45px;
            line-height: 1;
            font-weight: normal;
            color: #013087;
            text-align: center;
        }
`
    return (
            <VideoFeedSection className='some-space'>
				<h2>Video Feed</h2>
                <iframe allowFullScreen
                        title = 'camera feed'
                        webkitallowfullscreen="true"
                        mozallowfullscreen="
                        true"
			// !!! TO CHANGE !!!
                        src="http://127.0.0.1:5000/receive_data"
                        frameBorder="0"
                        width="100%"
                        height="576" />
			</VideoFeedSection>
    );
};

export default VideoFeed;
