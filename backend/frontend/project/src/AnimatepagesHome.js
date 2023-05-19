import {motion} from 'framer-motion'

const animation = {
    initial:{opacity: 0 , },
    animate : {opacity: 1,},
    exit  :{opacity: 0 , }
}

function Animatepages({children}) {
    return (
        <motion.div
            variants={animation}
            initial="initial"
            animate="animate"
            exit="exit"
            transition={{duration:1}}
        >
            {children}
        </motion.div>
    )
}

export default Animatepages