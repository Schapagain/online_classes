class FontChooser extends React.Component {

    constructor(props) {
		super(props);
		this.state = {
			bold: props.bold == 'true',
			size: Number(props.size)<Number(props.min)? Math.max(Number(props.min),1):Number(props.size),
			minSize: Math.max(Number(props.min),1),
			maxSize: Math.max(Number(props.max),Number(props.min),1,Number(props.size)),
			formHidden: true,
			text: props.text,
		}
		this.baseSize = Number(props.size);
		this.handleCheckboxChange = this.handleCheckboxChange.bind(this);
		this.handleTextClick = this.handleTextClick.bind(this);
		this.handleFontDecrease = this.handleFontDecrease.bind(this);
		this.handleFontIncrease = this.handleFontIncrease.bind(this);
		this.handleFontReset = this.handleFontReset.bind(this);
    }
	
	handleCheckboxChange(event) {
		this.setState({
			bold: !this.state.bold,
		})
	}

	handleTextClick(event) {
		this.setState({
			formHidden: !this.state.formHidden,
		})
	}

	handleFontDecrease (event) {
		console.l
		if (this.state.size > this.state.minSize){
			this.setState({
				size: this.state.size - 1
			})
		}
	}

	handleFontIncrease (event) {

		if (this.state.size < this.state.maxSize){
			this.setState({
				size: this.state.size + 1
			})
		}
	}

	handleFontReset (event) {
		this.setState({
			size: this.baseSize
		})
	}

    render() {

	return(
	       <div>
		   <input onChange={this.handleCheckboxChange}
		   checked={this.state.bold} type="checkbox" id="boldCheckbox" hidden={this.state.formHidden}/>
	       <button id="decreaseButton" onClick={this.handleFontDecrease} hidden={this.state.formHidden}>-</button>
	       <span id="fontSizeSpan" onDoubleClick={this.handleFontReset} style={{color: (this.state.size == this.state.maxSize || this.state.size == this.state.minSize)? 'red':'black'}} hidden={this.state.formHidden}>{this.state.size}</span>
	       <button id="increaseButton" onClick={this.handleFontIncrease} hidden={this.state.formHidden}>+</button>
			<span onClick={this.handleTextClick} id="textSpan" style={{fontSize: this.state.size,fontWeight: this.state.bold?'bold':'normal'}}>
				{this.state.text}
			</span>
	       </div>
	);
    }
}

